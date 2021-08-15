/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.UnknownHostException;
import java.nio.ByteBuffer;
import java.nio.channels.DatagramChannel;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author nightmare
 */
public class Client {
    public static void main(String[] args) {
        try(DatagramChannel channel = DatagramChannel.open()){ // Create datagram Socket Channel which get closed automatically when done
            // Binding the socket to a port
            channel.socket().bind(new InetSocketAddress(8801));
            // Buffer to store incoming message
            ByteBuffer buffer = ByteBuffer.allocate(1024);
            // receive message from socket
            channel.receive(buffer);
            // flip buffer to get bytes on right order
            buffer.flip();
            // Byte array to hold stream from bytebuffer
            byte[] data = new byte[buffer.remaining()];
            // Read buffer
            buffer.get(data);
            // Print
            System.out.println(new String(data));
            // Clear byte array
            data = null;
            // Clear buffer to reuse
            buffer.clear();
        } catch (UnknownHostException ex) {
            Logger.getLogger(Client.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(Client.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
