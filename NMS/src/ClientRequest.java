
public class ClientRequest {
	public RequestType Type;

	public static ClientRequest parseRequest(String request) {
		/* dirty way to tokenize shit without breaking quoted strings */
		String[] tokens = request.split("\\s+(?=([^\"]*\"[^\"]*\")*[^\"]*$)");
		/* even dirtier way of getting rid of quotes */
		for (int i = 0; i < tokens.length; i++)
			tokens[i] = tokens[i].replaceAll("^\"+", "").replaceAll("\"+$", "");

		if (tokens[0].equalsIgnoreCase("set")) {
			if (tokens.length != 4)
				return new InvalidRequest("can't parse Set request");
			System.out.printf("SET: dev=\"%s\", oid=\"%s\", val=\"%s\"\n", tokens[1],
					tokens[2], tokens[3]);
			return new SetRequest(tokens[1], tokens[2], tokens[3]);
		} else if (tokens[0].equalsIgnoreCase("get")) {
			if (tokens.length != 3)
				return new InvalidRequest("can't parse Get request");
			System.out.printf("GET: dev=\"%s\", oid=\"%s\"\n", tokens[1],
					tokens[2]);
			return new GetRequest(tokens[1], tokens[2]);
		} else if (tokens[0].equalsIgnoreCase("devices")) {
			System.out.printf("DEVICES:\n");
			return new DevicesRequest();
		} else if (tokens[0].equalsIgnoreCase("list")) {
			if (tokens.length != 2)
				return new InvalidRequest("can't parse List request");
			System.out.printf("List: dev=\"%s\"\n", tokens[1]);
			return new ListRequest(tokens[1]);
		} else if (tokens[0].equalsIgnoreCase("name")) {
			if (tokens.length != 3)
				return new InvalidRequest("can't parse Name request");
			System.out.printf("List: dev=\"%s\", oid=\"%s\"\n", tokens[1], tokens[2]);
			return new NameRequest(tokens[1], tokens[2]);
		} else if (tokens[0].equals("?") || tokens[0].equalsIgnoreCase("help")) {
			return new HelpRequest();
		} else
			return new InvalidRequest("can't parse request");
	}
}
