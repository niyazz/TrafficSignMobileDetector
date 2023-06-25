package org.tensorflow.lite.examples.detection.tflite;

import android.content.res.AssetManager;
import java.io.IOException;

public class DetectorFactory {
    public static YoloV5Classifier getDetector(
            final AssetManager assetManager,
            final String modelFilename)
            throws IOException {
        String labelFilename = null;
        boolean isQuantized = false;
        int inputSize = 640;

        if (modelFilename.equals("yolov5-fp16.tflite")) {
            labelFilename = "file:///android_asset/customclasses8.txt";
        }
        else if (modelFilename.equals("best-fp16.tflite")) {
            labelFilename = "file:///android_asset/customclasses.txt";;
        }
        return YoloV5Classifier.create(assetManager, modelFilename, labelFilename, isQuantized,
                inputSize);
    }

}
