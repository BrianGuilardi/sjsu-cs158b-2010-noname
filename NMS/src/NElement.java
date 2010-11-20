import java.util.TreeMap;

public class NElement {
	public String name;
	private TreeMap<String, String> mib;
	private TreeMap<String, String> names;
	
	public String getList() {
		StringBuffer oids = new StringBuffer();
		for(String oid: mib.keySet())
			oids.append(oid + " ");
		return oids.toString();
	}
	
	public String getValue(String oid) {
		return mib.get(oid);
	}
	
	public String getName(String oid) {
		return names.get(oid);
	}
	
	public void setValue(String oid, String value) {
		mib.put(oid, value);
	}
	
	public NElement(String name) {
		this.name = name;
		mib = new TreeMap<String, String>();
		names = new TreeMap<String, String>();
		MIB.Mib2_Ip ip = new MIB.Mib2_Ip();
		MIB.Mib2_Tcp tcp = new MIB.Mib2_Tcp();
		MIB.Mib2_Udp udp = new MIB.Mib2_Udp();
		for(MIB.MIB x: new MIB.MIB[] {ip, tcp, udp}) {
			for(String oid: x.getMap().keySet())
				mib.put(oid, x.getMap().get(oid));
			for(String oid: x.getMapNames().keySet())
				names.put(oid, x.getMapNames().get(oid));
		}
	}
}
