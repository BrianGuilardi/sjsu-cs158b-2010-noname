
public class InvalidRequest extends ClientRequest {
	private String error;
	
	public String getError() {
		return error;
	}

	public InvalidRequest(String error) {
		this.error = error;
		super.Type = RequestType.Invalid;
	}
}
