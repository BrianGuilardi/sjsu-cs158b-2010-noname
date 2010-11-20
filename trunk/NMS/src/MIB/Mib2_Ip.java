package MIB;

import java.util.Random;
import java.util.Set;
import java.util.TreeMap;

public class Mib2_Ip implements MIB {
	
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

	public Mib2_Ip() {
		oids = new TreeMap<String, String>();
		names = new TreeMap<String, String>();
		
		
		final Random rand = new Random();
		final String[][] data = { 
				{"1", "ipForwarding", "1"},
				{"2", "ipDefaultTTL", "64"},
				{"3", "ipInReceives", rand.nextInt(MAX) + ""},
				{"4", "ipInHdrErrors", rand.nextInt(MAX) + ""},
				{"5", "ipInAddrErrors", rand.nextInt(MAX) + ""},
				{"6", "ipForwDatagrams", rand.nextInt(MAX) + ""},
				{"7", "ipInUnknownProtos", rand.nextInt(MAX) + ""},
				{"8", "ipInDiscards", rand.nextInt(MAX) + ""},
				{"9", "ipInDelivers", rand.nextInt(MAX) + ""},
				{"10", "ipOutRequests", rand.nextInt(MAX) + ""},
				{"11", "ipOutDiscards", rand.nextInt(MAX) + ""},
				{"12", "ipOutNoRoutes", rand.nextInt(MAX) + ""},
				{"13", "ipReasmTimeout", rand.nextInt(MAX) + ""},
				{"14", "ipReasmReqds", rand.nextInt(MAX) + ""},
				{"15", "ipReasmOKs", rand.nextInt(MAX) + ""},
				{"16", "ipReasmFails", rand.nextInt(MAX) + ""},
				{"17", "ipFragOKs", rand.nextInt(MAX) + ""},
				{"18", "ipFragFails", rand.nextInt(MAX) + ""},
				{"19", "ipFragCreates", rand.nextInt(MAX) + ""},
				{"20", "ipAddrTable", rand.nextInt(MAX) + ""},
				{"21", "ipRouteTable", rand.nextInt(MAX) + ""},
				{"22", "ipNetToMediaTable", rand.nextInt(MAX) + ""},
				{"23", "ipRoutingDiscards", rand.nextInt(MAX) + ""},
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
		names.put("1.3.6.1.2.1.4", "IP");

	}
	
	private TreeMap<String, String> oids;
	private TreeMap<String, String> names;
	private final String prefix = "1.3.6.1.2.1.4.";
}
