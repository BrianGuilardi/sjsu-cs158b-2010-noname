package Request;

public class LoginRequest extends ClientRequest {
	public LoginRequest(String user, String password) {
		super();
		this.user = user;
		this.password = password;
		super.Type = RequestType.Login;
	}
	
	public String getUser() {
		return user;
	}
	
	public String getPassword() {
		return password;
	}
	
	public String user;
	public String password;
}
