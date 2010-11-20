
public class NameRequest extends ClientRequest {
	private String oid;
	private String device;
	
	public String getOid() {
		return oid;
	}
	
	public String getElementName() {
		return device;
	}
	
	public NameRequest(String device, String oid) {
		super();
		this.device = device;
		this.oid = oid;
		super.Type = RequestType.Name;
	}
}
