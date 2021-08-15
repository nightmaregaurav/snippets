/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author nightmare
 */
public class Server {
    public static void main(String[] args) {
        try {
            DatagramSocket datagramSocket = new DatagramSocket(8800);
            InetAddress clientAddress = InetAddress.getLocalHost();
            int i;
            for(i=0;i<2000;i++){
                byte[] sendBuffer = ("" + i).getBytes();
                DatagramPacket datagramPacketSendBuffer = new DatagramPacket(sendBuffer, sendBuffer.length, clientAddress, 4444);
                datagramSocket.send(datagramPacketSendBuffer);
            }
            datagramSocket.close();
        } catch (SocketException ex) {
            Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
