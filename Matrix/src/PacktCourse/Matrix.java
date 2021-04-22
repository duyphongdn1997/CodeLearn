package PacktCourse;
import java.math.*;
import java.util.*;
import java.lang.String;

class Matrix{
    private int n;
    private float[][] arr;

    public Matrix(){
        Scanner sc = new Scanner(System.in);
        System.out.println("N = ");
        this.n = sc.nextInt();
        nhapMatrix();
    }

    public Matrix(int n){
        this.n = n;
        nhapMatrix();
    }

    public void nhapMatrix(){
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                System.out.println("Arr[" + j + "]["+ i + "] = ");
                this.arr[i][j] = sc.nextFloat();
            }
        }
    }

    public Matrix(int n, float[][] arr){
        this.n = n;
        this.arr = arr;
    }
    public void setN(int n) {
        this.n = n;
    }

    public void setArr(float[][] arr) {
        this.arr = arr;
    }

    public int getN() {
        return n;
    }

    public float[][] getArr() {
        return arr;
    }

    public static void showArr(float[][] arr){
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                System.out.print(arr[i][j] + "\t");
            }
            System.out.println("\n");
        }
    }
    public static void showArr(float[] vector){
        for (int i = 0; i <vector.length;i++){
            System.out.print(vector[i]+"\t");
        }
        System.out.println("\n");
    }

    public static float[][] squareMatrix(int n, float[][] arr){
        float[][] C = new float[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                C[i][j] = 0;
                for (int k = 0; k < n; k++) {
                    C[i][j] = C[i][j] + arr[i][k] * arr[k][j];
                }
            }
        }
        return C;
    }

    public static float[] sumInRow(int n, float[][] arr){
        float[] sum = new float[n];
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                sum[i] += arr[i][j];
            }
        }
        return sum;
    }

    public static float[] vectoBoTrongSo(float[] sum){
        float sumTemp = 0;
        for (float v : sum) {
            sumTemp += v;
        }
        float[] sumVecto = new float[sum.length];
        for (int i = 0; i < sum.length; i++){
            sumVecto[i] = sum[i] / sumTemp;
        }
        return sumVecto;
    }

    public static float[] validateSumVecto(float[] sumVecto0, float[] sumVecto1){
        float[] validateVecto = new float[sumVecto0.length];
        for (int i = 0; i < sumVecto1.length; i++){
            validateVecto[i] = Math.abs(sumVecto0[i] - sumVecto1[i]);
        }
        return validateVecto;
    }

    public boolean compareVecto(float[] vecto0){
        for (float v : vecto0) if (v > 0.0002) return true;
        return false;
    }

    public float[] vector() {
        float[] vecto = new float[n];
        float[] sumEachRow = new float[n];
        float[] vecto1;
        do {
            vecto1 = new float[n];
            arr = squareMatrix(n, arr);
            sumEachRow = sumInRow(n, arr);
            vecto = vecto1;
            vecto1 = vectoBoTrongSo(sumEachRow);
            showArr(vecto1);
        }
        while (compareVecto(validateSumVecto(vecto, vecto1)));
        return vecto1;
    }

}

class Main {

    public static void main(String[] args) {
        float[][] arr = new float[3][3];
        arr[0][0] = 1;
        arr[0][1] = 2;
        arr[0][2] = 3;
        arr[1][0] = 1;
        arr[1][1] = 2;
        arr[1][2] = 3;
        arr[2][0] = 1;
        arr[2][1] = 2;
        arr[2][2] = 3;
        Matrix M1 = new Matrix(3,arr);
//        Matrix.showArr(M1.getArr());
//        Matrix.showArr(Matrix.squareMatrix(M1.getN(),M1.getArr()));
        Matrix.showArr(Matrix.sumInRow(M1.getN(),Matrix.squareMatrix(M1.getN(),M1.getArr())));

        float[] vector = new float[3];
        Matrix.showArr(M1.vector());
    }
}
