/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author nightmare
 */
public class Client {
    public static void main(String[] args) {
        try {
            // Creating datagram socket and binding at port 8801
            DatagramSocket datagramSocket = new DatagramSocket(8801);
            // Get server address (localhost this time)
            InetAddress serverAddress = InetAddress.getLocalHost();
            // Sender thread
            SenderThread senderThread = new SenderThread(datagramSocket, serverAddress, 8800);
            // Receiver thread
            ReceiverThread receiverThread = new ReceiverThread(datagramSocket);
            // Start the thread
            senderThread.start();
            // Start the thread
            receiverThread.start();
        } catch (SocketException ex) {
            Logger.getLogger(Client.class.getName()).log(Level.SEVERE, null, ex);
        } catch (UnknownHostException ex) {
            Logger.getLogger(Client.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }
}
