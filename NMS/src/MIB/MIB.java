package MIB;

import java.util.Set;
import java.util.TreeMap;

public interface MIB {
	final int MAX = 1000000;
	public TreeMap<String, String> getMap();
	public TreeMap<String, String> getMapNames();
	public Set<String> getKeys();
}