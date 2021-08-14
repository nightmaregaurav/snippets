/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;

/**
 *
 * @author nightmare
 */
public class Subtractor extends UnicastRemoteObject implements SubtractorSkeleton {
    Subtractor() throws RemoteException{
        super();
    }
    
    @Override
    public int sub(int a, int b){
        // Actual operation
        return b-a;
    }
}
