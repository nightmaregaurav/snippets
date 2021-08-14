/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Socket.UDP.SingleThreaded;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author nightmare
 */
public class Client {
    public static void main(String[] args) {
        try {
            // Scanner to scan user input
            Scanner scanner = new Scanner(System.in);
            // Creating datagram socket and binding at port 4444
            DatagramSocket datagramSocket = new DatagramSocket(4444);
            // Get server address (localhost this time)
            InetAddress serverAddress = InetAddress.getLocalHost();
            // Buffer to store data to send
            byte[] sendBuffer = null;
            // Getting user input
            String input = scanner.nextLine();
            // Converting input to byte and storing in buffer
            sendBuffer = input.getBytes();
            // Converting buffer to datagram packet
            DatagramPacket datagramPacketSendBuffer = new DatagramPacket(sendBuffer, sendBuffer.length, serverAddress, 8800);
            // Sending the packet
            datagramSocket.send(datagramPacketSendBuffer);
            // Buffer to store received message
            byte[] receiveBuffer = new byte[1024];
            // Datagram Packet to receive and fill buffer
            DatagramPacket datagramPacketReceiveBuffer = new DatagramPacket(receiveBuffer, receiveBuffer.length);
            // Actual receiving process
            datagramSocket.receive(datagramPacketReceiveBuffer);
            // Printing the message
            System.out.println("Server said: " + new String(receiveBuffer));
            // Filling/Clearing the buffer
            receiveBuffer = new byte[1024];
            // Closing the socket connection
            datagramSocket.close();
        } catch (SocketException ex) {
            Logger.getLogger(Client.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(Client.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }
}
