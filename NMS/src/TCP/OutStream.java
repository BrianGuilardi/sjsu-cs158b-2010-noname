package TCP;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.Socket;

public class OutStream {
    private PrintWriter out;

    public OutStream(Socket socket) {
        try                     { out = new PrintWriter(socket.getOutputStream(), true); }
        catch (IOException ioe) { ioe.printStackTrace();                                 }
    }

    public void close() { out.close(); }


    public void println(Object x)  { out.println(x); out.flush(); }
}
