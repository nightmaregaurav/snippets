/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author nightmare
 */

public class Server {
    public static void main(String[] args) {
        try {
            // Create and bind ServerSocket
            ServerSocket serverSocket = new ServerSocket(8800);
            
            while(true){
                // Accept request from client
                Socket connection = serverSocket.accept();
                ReceiverThread receiverThread = new ReceiverThread(connection);
                SenderThread senderThread = new SenderThread(connection);
                receiverThread.start();
                senderThread.start();   
            }
        } catch (IOException ex) {
            Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
