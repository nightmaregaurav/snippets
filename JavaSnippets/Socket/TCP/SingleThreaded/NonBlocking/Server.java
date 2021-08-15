/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.ServerSocketChannel;
import java.nio.channels.SocketChannel;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author nightmare
 */
public class Server {
    public static void main(String[] args) {
        try{
            // Server socket Channel creation
            ServerSocketChannel ss = ServerSocketChannel.open();
            // Binding SS Channel to a port
            ss.socket().bind(new InetSocketAddress(8800));
            // Connection socket
            SocketChannel s = ss.accept();
            // Buffer to store incoming message
            ByteBuffer buffer = ByteBuffer.allocate(1024);
            // Read message from socket
            s.read(buffer);
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
            // Close connection with client
            s.close();
            // Close server socket
            ss.close();
        } catch (IOException ex) {
            Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
