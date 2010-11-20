package MIB;

import java.util.Random;
import java.util.Set;
import java.util.TreeMap;

public class Mib2_Tcp implements MIB {
	
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

	public Mib2_Tcp() {
		oids = new TreeMap<String, String>();
		names = new TreeMap<String, String>();
		
		final Random rand = new Random();
		final String[][] data = { 
				{"1", "tcpRtoAlgorithm", "2"},
				{"2", "tcpRtoMin", rand.nextInt(MAX) + ""},
				{"3", "tcpRtoMax", rand.nextInt(MAX) + ""},
				{"4", "tcpMaxConn", rand.nextInt(MAX) + ""},
				{"5", "tcpActiveOpens", rand.nextInt(MAX) + ""},
				{"6", "tcpPassiveOpens", rand.nextInt(MAX) + ""},
				{"7", "tcpAttemptFails", rand.nextInt(MAX) + ""},
				{"8", "tcpEstabResets", rand.nextInt(MAX) + ""},
				{"9", "tcpCurrEstab", rand.nextInt(MAX) + ""},
				{"10", "tcpInSegs", rand.nextInt(MAX) + ""},
				{"11", "tcpOutSegs", rand.nextInt(MAX) + ""},
				{"12", "tcpRetransSegs", rand.nextInt(MAX) + ""},
				{"13", "tcpConnTable", rand.nextInt(MAX) + ""},
				{"14", "tcpInErrs", rand.nextInt(MAX) + ""},
				{"15", "tcpOutRsts", rand.nextInt(MAX) + ""},
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
		names.put("1.3.6.1.2.1.6", "TCP");

	}
	
	private TreeMap<String, String> oids;
	private TreeMap<String, String> names;
	private final String prefix = "1.3.6.1.2.1.6.";
}
