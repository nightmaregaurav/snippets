/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author nightmare
 */
class SenderThread extends Thread{
    DatagramSocket connection;
    InetAddress receiverAddress;
    int port;
    Scanner scanner;
    public SenderThread(DatagramSocket connection, InetAddress receiverAddress, int port){
        this.connection = connection;
        this.receiverAddress = receiverAddress;
        this.port = port;
        scanner = new Scanner(System.in);
    }
    
    @Override
    public void run(){
        // Buffer to store data to send
        byte[] buffer = new byte[1024];
        while(true){
            try {
                // Getting user input
                String input = scanner.nextLine();
                // Converting input to byte and storing in buffer
                buffer = input.getBytes();
                // Converting buffer to datagram packet
                DatagramPacket datagramPacket = new DatagramPacket(buffer, buffer.length, receiverAddress, port);
                // Sending the packet
                connection.send(datagramPacket);
                // Filling/Clearing the buffer
                buffer = new byte[1024];
            } catch (IOException ex) {
                Logger.getLogger(SenderThread.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
    }
}

class ReceiverThread extends Thread{
    DatagramSocket connection;
    public ReceiverThread(DatagramSocket connection){
        this.connection = connection;
    }
    
    @Override
    public void run(){
        // Buffer to store received message
        byte[] buffer = new byte[1024];
        while(true){
            try {
                // Datagram Packet to receive and fill buffer
                DatagramPacket datagramPacket = new DatagramPacket(buffer, buffer.length);
                // Actual receiving process
                connection.receive(datagramPacket);
                // Printing the message
                System.out.println(datagramPacket.getAddress() + ":" + datagramPacket.getPort() + " --> " + new String(buffer));
                // Filling/Clearing the buffer
                buffer = new byte[1024];
            } catch (IOException ex) {
                Logger.getLogger(SenderThread.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
    }
}
