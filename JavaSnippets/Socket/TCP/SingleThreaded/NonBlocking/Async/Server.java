/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.AsynchronousServerSocketChannel;
import java.nio.channels.AsynchronousSocketChannel;
import java.nio.channels.CompletionHandler;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author nightmare
 */
public class Server {
    public static void main(String[] args) {
        try(AsynchronousServerSocketChannel ss = AsynchronousServerSocketChannel.open()){ // Async Server socket Channel creation and setup for Close=ing connection with all client and close server socket after done
            // Binding SS Channel to a port
            ss.bind(new InetSocketAddress(8800));
            // Accept connection Asynchronously
            ss.accept(null, new CompletionHandler<AsynchronousSocketChannel, Void>(){
                @Override
                public void completed(AsynchronousSocketChannel s, Void A) {
                    try (s) { // Close connection with client after executing
                        // accept the next connection
                        ss.accept(null, this);                        
                        // handle this connection
                        handle(s);
                    } catch (IOException ex) {
                        Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex);
                    }
                }
                public void handle(AsynchronousSocketChannel s) throws IOException{
                    // Buffer to store incoming message
                    ByteBuffer buffer = ByteBuffer.allocate(1024);
                    // Read message from socket
                    s.read(buffer, null, new CompletionHandler<Integer, Void>() {
                        @Override
                        public void completed(Integer v, Void a) {
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
                        }
                        @Override
                        public void failed(Throwable ex, Void a) {
                            Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex);
                        }
                    });
                    
                    // Do other stuff here, they don't wait above code to complete so if there is nothing below, use infinite loop or scanline or user choosen exit system
                    while(true){}
                }
                @Override
                public void failed(Throwable ex, Void A) {
                    Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex);
                }
            });

            // Do other stuff here, they don't wait above code to complete so if there is nothing below, use infinite loop or scanline or user choosen exit system
            new Scanner(System.in).nextLine();
        } catch (IOException ex) {
            Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
