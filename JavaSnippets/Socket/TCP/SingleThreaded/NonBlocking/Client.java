/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.SocketChannel;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author nightmare
 */
public class Client {
    public static void main(String[] args) {
        try{
            // Create and open socket channel
            SocketChannel s = SocketChannel.open();
            // Connect to server
            s.connect(new InetSocketAddress("localhost", 8800));
            // Create message bytebuffer
            ByteBuffer buffer = ByteBuffer.wrap(new Scanner(System.in).nextLine().getBytes());
            // fit message in buffer
            buffer.compact();
            // Flip buffer to turn in in right order
            buffer.flip();
            // Send buffer message to server
            s.write(buffer);
            // Clear buffer to reuse
            buffer.clear();
            // close connection
            s.close();
        } catch (IOException ex) {
            Logger.getLogger(Client.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
