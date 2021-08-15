/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.DataInputStream;
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
        try {
            // Create socket connection to server
            Socket connection = new Socket("localhost", 8800);
            // Thread to receiv messages
            ReceiverThread receiverThread = new ReceiverThread(connection);
            // Thread to send messages
            SenderThread senderThread = new SenderThread(connection);
            // Start receiving
            receiverThread.start();
            // Start sending
            senderThread.start(); 
        } catch (IOException ex) {
            Logger.getLogger(Client.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}

class ReceiverThread extends Thread{
    Socket connection;
    public ReceiverThread(Socket connection){
        this.connection = connection;
    }
    
    @Override
    public void run(){
        DataInputStream in = null;
        while(true){
            try {
                // Stream to receive message
                in = new DataInputStream(connection.getInputStream());
                // Print msg
                System.out.println(in.readUTF());
                
            } catch (IOException ex) {
                try {
                    // Prepare Message
                    String msg = "Server at " + connection.toString() + " Dead, Exiting...";
                    // Print on client console
                    System.out.println(msg);
                    // Close the stream
                    in.close();
                    // Close the connection
                    connection.close();
                } catch (IOException ex1) {
                    Logger.getLogger(Client.class.getName()).log(Level.SEVERE, null, ex1);
                } finally {
                    System.exit(0);
                }
            }
        }
    }
}
