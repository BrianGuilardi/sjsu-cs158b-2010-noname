import java.net.Socket;
import java.io.IOException;
import java.io.InputStream;
import java.io.BufferedInputStream;
import java.util.Scanner;
import java.util.Locale;


public final class InStream {
    private Scanner scanner;
    private String charsetName = "ISO-8859-1";
    private Locale usLocale = new Locale("en", "US");


    public InStream(Socket socket) {
        try {
            InputStream is = socket.getInputStream();
            scanner = new Scanner(new BufferedInputStream(is), charsetName);
            scanner.useLocale(usLocale);
        }
        catch (IOException ioe) {
            System.err.println("Could not open " + socket);
        }
    }

    public String readLine() {
        String line = null;
        try                 { line = scanner.nextLine(); }
        catch (Exception e) {                            }
        return line;
    }

    public void close() { scanner.close();  }

}