class AudioProcessor extends AudioWorkletProcessor {
    constructor() {
        super();
    }

    process(inputs, outputs, parameters) {
        const input = inputs[0];
        const frameData = new Float32Array(input[0]);
        this.port.postMessage({ frameData });
        return true;
    }
}

registerProcessor('audio-processor', AudioProcessor);
