/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.SocketException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author nightmare
 */
public class Client {
    public static void main(String[] args) {
        try {
            DatagramSocket datagramSocket = new DatagramSocket(4444);
            byte[] receiveBuffer = new byte[1024];
            for(;;){
                DatagramPacket datagramPacketReceiveBuffer = new DatagramPacket(receiveBuffer, receiveBuffer.length);
                datagramSocket.receive(datagramPacketReceiveBuffer);
                System.out.println("Server said: " + new String(receiveBuffer));
                receiveBuffer = new byte[1024];
            }
        } catch (SocketException ex) {
            Logger.getLogger(Client.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(Client.class.getName()).log(Level.SEVERE, null, ex);
        }    
    }
}
