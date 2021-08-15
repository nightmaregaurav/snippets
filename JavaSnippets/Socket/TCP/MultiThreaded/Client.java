/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

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
            ReceiverThread receiverThread = new ReceiverThread(connection);
            SenderThread senderThread = new SenderThread(connection);
            receiverThread.start();
            senderThread.start(); 
        } catch (IOException ex) {
            Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
