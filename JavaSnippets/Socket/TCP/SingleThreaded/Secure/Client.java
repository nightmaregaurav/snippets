/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.Writer;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.net.ssl.SSLSocket;
import javax.net.ssl.SSLSocketFactory;

/**
 *
 * @author nightmare
 */
public class Client {
    public static void main(String[] args) {
        try{
            // secure socket factory instance
            SSLSocketFactory factory = (SSLSocketFactory) SSLSocketFactory.getDefault();
            // create secure socket
            SSLSocket socket = (SSLSocket) factory.createSocket("localhost", 8800);
            // writer to write to server
            Writer out = new OutputStreamWriter(socket.getOutputStream(), "UTF-8");
            // write message
            out.write("Hello server");
            // Close connection
            socket.close();
        } catch (IOException ex) {
            Logger.getLogger(Client.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
