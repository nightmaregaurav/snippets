/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.Socket;
import java.security.KeyManagementException;
import java.security.KeyStore;
import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;
import java.security.UnrecoverableKeyException;
import java.security.cert.CertificateException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.net.ssl.KeyManagerFactory;
import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLServerSocket;
import javax.net.ssl.SSLServerSocketFactory;

/**
 *
 * @author nightmare
 */
public class Server {
    public static void main(String[] args) {
        try{
            // Create SSL context
            SSLContext context = SSLContext.getInstance("SSL");
            // get SSL Key manager Factory instance
            KeyManagerFactory kmf = KeyManagerFactory.getInstance("SunX509");
            // Create SSL keystore
            KeyStore ks = KeyStore.getInstance("JKS");
            // password for ssl cert
            char[] password = {'a','b','c'};
            // load ssl cert from file with passwprd
            ks.load(new FileInputStream("jnp4e.keys"), password);
            // initialise the ssl key manager factory
            kmf.init(ks, password);
            // initialise the ssl context
            context.init(kmf.getKeyManagers(), null, null);
            // get secure server sock factory instance
            SSLServerSocketFactory factory = context.getServerSocketFactory();
            // create secure server socket
            SSLServerSocket server = (SSLServerSocket) factory.createServerSocket(8800);
            // Accept conn from client
            Socket theConnection = server.accept();
            // Stream t oreceive the data
            DataInputStream in = new DataInputStream(theConnection.getInputStream());
            // print out the data
            System.out.println(new String(in.readAllBytes()));
        } catch (NoSuchAlgorithmException ex) {
            Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex);
        } catch (KeyStoreException ex) {
            Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex);
        } catch (CertificateException ex) {
            Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex);
        } catch (UnrecoverableKeyException ex) {
            Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex);
        } catch (KeyManagementException ex) {
            Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
