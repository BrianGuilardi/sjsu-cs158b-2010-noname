package Request;

public class SetRequest extends ClientRequest {
	public SetRequest(String EName, String OID, String Value) {
		super();
		this.ElementName = EName;
		this.OID = OID;
		this.Value = Value;
		super.Type = RequestType.Set;
	}
	
	public String getElementName() {
		return ElementName;
	}
	
	public String getOID() {
		return OID;
	}
	
	public String getValue() {
		return Value;
	}
	private String ElementName;
	private String OID;
	private String Value;
	
}
