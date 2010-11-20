
public class ListRequest extends ClientRequest {
	private String device;
	
	public String getElementName() {
		return device;
	}
	
	public ListRequest(String device) {
		super();
		this.device = device;
		super.Type = RequestType.List;
	}
}
