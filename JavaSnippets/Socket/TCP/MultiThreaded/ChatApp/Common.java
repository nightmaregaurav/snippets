/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

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
        while(true){
            // Get input to send message
            String message = scanner.nextLine();
            // Send message
            send(this.connection, message);
        }
    }
    
    public static void send(Socket Conn, String message) {
        DataOutputStream out = null;
        try {
            // Stream to send message
            out = new DataOutputStream(Conn.getOutputStream());
            // Send message
            out.writeUTF(message);
        } catch (IOException ex) {
            Logger.getLogger(SenderThread.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}