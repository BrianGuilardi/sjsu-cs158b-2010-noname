package AccessControl;

public enum User {
	ANONYMOUS("Default anonymous user with pretty much now permissions"),
	GUEST("Guest user with read-only permissions"),
	ADMIN("Administrator with read/write permissions");
	
	User(String desc) {
		this.desc = desc;
	}
	public String desc;
}
