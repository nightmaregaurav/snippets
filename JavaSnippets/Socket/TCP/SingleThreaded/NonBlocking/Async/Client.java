/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.AsynchronousSocketChannel;
import java.nio.channels.CompletionHandler;
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
            AsynchronousSocketChannel s = AsynchronousSocketChannel.open();
            // Connect to server
            s.connect(new InetSocketAddress("localhost", 8800), null, new CompletionHandler<Void, Void>(){
                @Override
                public void completed(Void v, Void a) {
                    try(s) { // close connection automatically after done
                        // Create message bytebuffer
                        ByteBuffer buffer = ByteBuffer.wrap(new Scanner(System.in).nextLine().getBytes());
                        // fit message in buffer
                        buffer.compact();
                        // Flip buffer to turn in in right order
                        buffer.flip();
                        // Send buffer message to server
                        s.write(buffer, null, new CompletionHandler<Integer, Void>() {
                            @Override
                            public void completed(Integer v, Void a) {
                                // Clear buffer to reuse
                                buffer.clear();
                                // Exit after done
                                System.exit(0);
                            }
                            @Override
                            public void failed(Throwable ex, Void a) {
                                Logger.getLogger(Client.class.getName()).log(Level.SEVERE, null, ex);
                            }
                        });
                    } catch (IOException ex) {
                        Logger.getLogger(Client.class.getName()).log(Level.SEVERE, null, ex);
                    }
                }
                @Override
                public void failed(Throwable ex, Void a) {
                    Logger.getLogger(Client.class.getName()).log(Level.SEVERE, null, ex);
                }
            });
            
            // Do other stuff here, they don't wait above code to complete so if there is nothing below, use infinite loop or user choosen exit system
            while(true){}
        } catch (IOException ex) {
            Logger.getLogger(Client.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}