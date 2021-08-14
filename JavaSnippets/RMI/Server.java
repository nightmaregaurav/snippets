/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.Remote;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author nightmare
 */
public class Server {
    String host;
    int port;
    public Server(String host, int port) throws RemoteException {
        // Hostname to use on server
        this.host = host;
        // Port to use as server
        this.port = port;
        
        // Create registry and register port
        LocateRegistry.createRegistry(this.port);
    }
    
    public void serve(Remote skeleton, String path) throws RemoteException, MalformedURLException{
        // Binding the object to host port and path
        Naming.rebind("rmi://" + host + ":" + port + path, skeleton);
    }
    
    public static void main(String[] args) {
        try {
            String host = "localhost";
            int port = 5000;
            // Creating server object
            Server server = new Server(host, port);
          
            // Create skeleton object from actual implementation
            AdderSkeleton skeleton1 = (AdderSkeleton) new Adder();
            // Serve the skeleton from server
            server.serve(skeleton1, "/adder");
            
            // Create skeleton object from actual implementation
            SubtractorSkeleton skeleton2 = (SubtractorSkeleton) new Subtractor();
            // Serve the skeleton from server
            server.serve(skeleton2, "/subtractor");
        } catch (RemoteException | MalformedURLException ex) {
            Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
