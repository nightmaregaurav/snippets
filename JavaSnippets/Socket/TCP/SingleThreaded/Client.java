/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author nightmare
 */
public class Client {
    public static void main(String[] args) {
        // Create socket connection to server using try with resource so we won't need to close it later
        try (Socket socket = new Socket("localhost", 8800)) {
            // Stream to send message to server
            DataOutputStream out = new DataOutputStream(socket.getOutputStream());
            // Send message
            out.writeUTF("Client said hi!");
            // Stream to get message from server
            DataInputStream in = new DataInputStream(socket.getInputStream());
            // Print msg
            System.out.println(socket.getRemoteSocketAddress() + " --> " + in.readUTF());
            // Close Connection
        } catch (IOException ex) {
        Logger.getLogger(Client.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }
}
