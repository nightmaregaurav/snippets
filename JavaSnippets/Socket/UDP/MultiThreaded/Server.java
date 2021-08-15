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
public class Server {
    public static void main(String[] args) {
        try {
            // Creating datagram socket and binding at port 8800
            DatagramSocket datagramSocket = new DatagramSocket(8800);
            // Get client address (localhost this time)
            InetAddress ClientAddress = InetAddress.getLocalHost();
            // Sender thread
            SenderThread senderThread = new SenderThread(datagramSocket, ClientAddress, 8801);
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
