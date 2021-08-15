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
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author nightmare
 */
public class Server {
    public static void main(String[] args) {
        try(DatagramChannel channel = DatagramChannel.open()){ // Create datagram Socket Channel which get closed automatically when done
            // Binding the socket to a port
            channel.socket().bind(new InetSocketAddress(8800));
            // Create message bytebuffer
            ByteBuffer buffer = ByteBuffer.wrap(new Scanner(System.in).nextLine().getBytes());
            // fit message in buffer
            buffer.compact();
            // Flip buffer to turn in in right order
            buffer.flip();
            // Send buffer message to client
            channel.send(buffer, new InetSocketAddress("localhost", 8801));
        } catch (UnknownHostException ex) {
            Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
