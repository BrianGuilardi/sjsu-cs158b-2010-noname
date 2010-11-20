package MIB;

import java.util.Random;
import java.util.Set;
import java.util.TreeMap;

public class Mib2_Udp implements MIB {
	
	@Override
	public TreeMap<String, String> getMap() {
		return oids;
	}

	@Override
	public Set<String> getKeys() {
		return oids.keySet();
	}
	
	@Override
	public TreeMap<String, String> getMapNames() {
		return names;
	}

	public Mib2_Udp() {
		oids = new TreeMap<String, String>();
		names = new TreeMap<String, String>();
		
		final Random rand = new Random();
		final String[][] data = { 
				{"1", "udpInDatagrams", rand.nextInt(MAX) + ""},
				{"2", "udpNoPorts", rand.nextInt(MAX) + ""},
				{"3", "udpInErrors", rand.nextInt(MAX) + ""},
				{"4", "udpOutDatagrams", rand.nextInt(MAX) + ""},
				{"5", "udpTable", rand.nextInt(MAX) + ""},
		};
		
		for(String[] entry: data) {
			oids.put(prefix + entry[0], entry[2]);
			names.put(prefix + entry[0], entry[1]);
		}
		names.put("1", "ISO");
		names.put("1.3", "ORG");
		names.put("1.3.6", "DOD");
		names.put("1.3.6.1", "Internet");
		names.put("1.3.6.1.2", "Mgmt");
		names.put("1.3.6.1.2.1", "Mib-2");
		names.put("1.3.6.1.2.1.7", "UDP");

	}
	
	private TreeMap<String, String> oids;
	private TreeMap<String, String> names;
	private final String prefix = "1.3.6.1.2.1.6.";
}
