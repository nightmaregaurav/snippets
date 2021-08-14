/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.rmi.Remote;
import java.rmi.RemoteException;

/**
 *
 * @author nightmare
 */
public interface SubtractorSkeleton extends Remote {
    // Skeleton method
    int sub(int a, int b) throws RemoteException;
}
