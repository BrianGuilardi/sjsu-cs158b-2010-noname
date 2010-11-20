import java.util.TreeMap;
import java.net.Socket;
import java.net.ServerSocket;

public class NMServer {
  static TreeMap<String, NElement> elements = new TreeMap<String, NElement>();

  public static void main(String[] args) throws Exception {

    int port = 12345;
    ServerSocket serverSocket = new ServerSocket(port);
    System.err.printf("Listening on port: %d \n", port);
    
    populateNetwork();

    
    while (true) {

        Socket clientSocket = serverSocket.accept();
        System.err.println("Accepted connection from client");
        
        InStream  in  = new InStream(clientSocket);
        OutStream out = new OutStream(clientSocket);

        String s;
        while ((s = in.readLine()) != null) {
            String response = processRequest(ClientRequest.parseRequest(s));
            out.println(response);
        }

        System.err.printf("Closing connection with client\n");
        out.close();
        in.close();
        clientSocket.close();
    }
  }
  
  private static String processRequest(ClientRequest request) {
	  switch (request.Type) {
	  case Get: {
		  GetRequest req = (GetRequest) request;
		  if (!elements.containsKey(req.getElementName()))
			  return String.format("Error: %s device doesn't exist\n", req.getElementName());
		  NElement device = elements.get(req.getElementName());
		  return String.format("Success: %s\n", device.getValue(req.getOID()));
	  }
	  case Set: {
		  SetRequest req = (SetRequest) request;
		  if (!elements.containsKey(req.getElementName()))
			  return String.format("Error: %s device doesn't exist\n", req.getElementName());
		  NElement device = elements.get(req.getElementName());
		  device.setValue(req.getOID(), req.getValue());
		  return String.format("Success: value set.\n");
	  }
	  case Devices: {
		  StringBuffer devs = new StringBuffer();
		  for(String elem: elements.keySet())
			  devs.append(elem + " ");
		  return String.format("Success: %s\n", devs.toString());
	  }
	  case List: {
		  ListRequest req = (ListRequest) request;
		  if (!elements.containsKey(req.getElementName()))
			  return String.format("Error: %s device doesn't exist\n", req.getElementName());
		  NElement element = elements.get(req.getElementName());
		  return String.format("Success: %s\n", element.getList());
	  }
	  case Name: {
		  NameRequest req = (NameRequest) request;
		  if (!elements.containsKey(req.getElementName()))
			  return String.format("Error: %s device doesn't exist\n", req.getElementName());
		  NElement element = elements.get(req.getElementName());
		  return String.format("Success: %s\n", element.getName(req.getOid()));
	  }
	  case Help: {
		  StringBuffer sb = new StringBuffer();
		  sb.append("Help:\n");
		  for(RequestType req: RequestType.values()) {
			  sb.append(req.getHelpString() + "\n");
		  }
		  return String.format("%s", sb.toString());
	  }
	  case Invalid: {
		  InvalidRequest req = (InvalidRequest) request;
		  return String.format("Error: Unkown Request: %s\n", req.getError());
	  }
	  }
	  return String.format("Error: Unkown Request\n");
  }
  
  private static void populateNetwork() {
	  String[] devices = { "Cisco_3509", "Juniper_M120" };
	  for(String device: devices) {
		  elements.put(device, new NElement(device));
	  }
  }
}