package Request;

public enum RequestType {
	Set ("Set <dev> <oid> <val>		# set <val> of <oid> on a given <dev>"),
	Get ("Get <dev> <oid>			# get value of <oid> on a given <dev>"),
	Devices ("Devices				# list available network elements"),
	List ("list <dev>			# list available oids on a <dev>"),
	Name ("Name <dev> <oid>		# given <dev> and <oid>, return oid's string name"),
	Help ("Help				# HELPZZ!!"),
	Invalid ("");
	
	private final String help;
	RequestType(String help) {
		this.help = help;
	}

	public String getHelpString() {return help;}
}
