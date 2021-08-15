/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.DataInputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author nightmare
 */

public class Server {
    public static void main(String[] args) {
        new Server();
    }
    
    public Server(){
        ArrayList<Socket> ConnList = new ArrayList<Socket>();
        try {
            // Create and bind ServerSocket
            ServerSocket serverSocket = new ServerSocket(8800);
            
            while(true){
                // Accept request from client
                Socket connection = serverSocket.accept();
                // Prepare Message
                String message = connection.getRemoteSocketAddress().toString().substring(1) + " Joined the chat";
                // Notify all
                notifyAll(connection, ConnList, message);
                // Add to the list
                ConnList.add(connection);
                // Thread for forwarding message
                Thread forwardThread = new Thread(() -> {
                    DataInputStream in = null;
                        while(true){
                            try {
                                // Stream to receive message
                                in = new DataInputStream(connection.getInputStream());
                                // Set msg
                                String msg = connection.getRemoteSocketAddress().toString().substring(1) + " --> " + in.readUTF();
                                // Forward to all
                                notifyAll(connection, ConnList, msg);
                            } catch (IOException ex) {
                                try {
                                    // Prepare Message
                                    String msg = connection.getRemoteSocketAddress().toString().substring(1) + " Left the chat";
                                    // Notify all
                                    notifyAll(connection, ConnList, msg);
                                    // Close the stream
                                    in.close();
                                    // Close the connection
                                    connection.close();
                                } catch (IOException ex1) {
                                    Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex1);
                                } finally {
                                    // Remove the connection either way
                                    ConnList.remove(connection);
                                    // exit the thread
                                    return;
                                }
                            }
                        }
                });
                forwardThread.start();
            }
        } catch (IOException ex) {
            Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    public static void notifyAll(Socket connection, ArrayList<Socket> ConnList, String message) {
        // Print in server console
        System.out.println(message);
        for(Socket Conn : ConnList){
            // For all connection in list except initialiser itself
            if(!Conn.equals(connection))
                // Actual message sender
                send(Conn, message);
        }
    }
}