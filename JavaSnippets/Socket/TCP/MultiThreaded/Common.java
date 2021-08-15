/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author nightmare
 */
class SenderThread extends Thread{
    Socket connection;
    Scanner scanner;
    public SenderThread(Socket connection){
        this.connection = connection;
        scanner = new Scanner(System.in);
    }
    
    @Override
    public void run(){
        DataOutputStream out = null;
        while(true){
            try {
                // Stream to send message
                out = new DataOutputStream(connection.getOutputStream());
                // Get input to send message
                String message = scanner.nextLine();
                // Send message
                out.writeUTF(message);
            } catch (IOException ex) {
                Logger.getLogger(SenderThread.class.getName()).log(Level.SEVERE, null, ex);
            }
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
                System.out.println(connection.getRemoteSocketAddress() + " --> " + in.readUTF());
            } catch (IOException ex) {
                Logger.getLogger(SenderThread.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
    }
}
