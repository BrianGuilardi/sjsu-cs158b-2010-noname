import java.util.TreeMap;
import java.net.Socket;
import java.net.ServerSocket;
import AccessControl.User;
import Request.ClientRequest;
import Request.GetRequest;
import Request.InvalidRequest;
import Request.ListRequest;
import Request.LoginRequest;
import Request.NameRequest;
import Request.RequestType;
import Request.SetRequest;
import TCP.InStream;
import TCP.OutStream;

public class NMServer {
  static TreeMap<String, NElement> elements = new TreeMap<String, NElement>();
  /* by default, without logging in, everyone is considered to be an anonymous user */
  static User currentUser = User.ANONYMOUS;

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
        cleanup();
        out.close();
        in.close();
        clientSocket.close();
    }
  }
  
  private static void cleanup() {
	/* revert back to anonymous access */
	currentUser = User.ANONYMOUS;
}

private static String processRequest(ClientRequest request) {
	  switch (request.Type) {
	  case Login: {
		  LoginRequest req = (LoginRequest) request;
		  if (req.getUser().equals("root") || req.getUser().equals("admin")) {
				  if (req.getPassword().equals("admin")) {
					  currentUser = User.ADMIN;
					  return String.format("Success: %s logged in", req.getUser());
				  } else {
					  return String.format("Error: wrong credentials", req.getUser());
				  }		  
		  }
		  if (req.getUser().equals("guest")) {
				  currentUser = User.GUEST;
				  return String.format("Success: %s logged in", req.getUser());
		  }
		  return String.format("Error: %s unknown credentials", req.getUser());
	  }
	  case Get: {
		  if (!checkReadPermissions())
			  return String.format("Error: no Get access allowed for %s\n", currentUser);
		  GetRequest req = (GetRequest) request;
		  if (!elements.containsKey(req.getElementName()))
			  return String.format("Error: %s device doesn't exist\n", req.getElementName());
		  NElement device = elements.get(req.getElementName());
		  return String.format("Success: %s\n", device.getValue(req.getOID()));
	  }
	  case Set: {
		  if (!checkWritePermissions())
			  return String.format("Error: no Set access allowed for %s\n", currentUser);
		  
		  SetRequest req = (SetRequest) request;
		  if (!elements.containsKey(req.getElementName()))
			  return String.format("Error: %s device doesn't exist\n", req.getElementName());
		  NElement device = elements.get(req.getElementName());
		  device.setValue(req.getOID(), req.getValue());
		  return String.format("Success: value set.\n");
	  }
	  case Devices: {
		  if (!checkReadPermissions())
			  return String.format("Error: no Devices access allowed for %s\n", currentUser);
		  StringBuffer devs = new StringBuffer();
		  for(String elem: elements.keySet())
			  devs.append(elem + " ");
		  return String.format("Success: %s\n", devs.toString());
	  }
	  case List: {
		  if (!checkReadPermissions())
			  return String.format("Error: no List access allowed for %s\n", currentUser);
		  ListRequest req = (ListRequest) request;
		  if (!elements.containsKey(req.getElementName()))
			  return String.format("Error: %s device doesn't exist\n", req.getElementName());
		  NElement element = elements.get(req.getElementName());
		  return String.format("Success: %s\n", element.getList());
	  }
	  case Name: {
		  if (!checkWritePermissions())
			  return String.format("Error: no Name access allowed for %s\n", currentUser);
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
  
private static boolean checkWritePermissions() {
	return currentUser == User.ADMIN;
}

private static boolean checkReadPermissions() {
	return (currentUser == User.GUEST) || (currentUser == User.ADMIN);
}

private static void populateNetwork() {
	  String[] devices = { "Cisco_3509", "Juniper_M120" };
	  for(String device: devices) {
		  elements.put(device, new NElement(device));
	  }
  }
}

