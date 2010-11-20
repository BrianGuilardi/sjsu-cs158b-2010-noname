package Request;

public class HelpRequest extends ClientRequest {
	public HelpRequest() {
		super();
		super.Type = RequestType.Help;
	}
}
