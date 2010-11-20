
public class GetRequest extends ClientRequest {
	public GetRequest(String EName, String OID) {
		super();
		this.ElementName = EName;
		this.OID = OID;
		super.Type = RequestType.Get;
	}
	
	public String getElementName() {
		return ElementName;
	}
	
	public String getOID() {
		return OID;
	}
	
	private String ElementName;
	private String OID;
}
