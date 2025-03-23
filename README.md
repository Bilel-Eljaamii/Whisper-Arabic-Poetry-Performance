# Whisper-Arabic-Poetry-Performance
🗣️ Benchmarking OpenAI Whisper for Classical Arabic Poetry Transcription
A comprehensive analysis of Whisper ASR models (tiny to turbo) for transcribing classical Arabic texts like Amr ibn Kulthum's Mu'allaqat. Includes performance metrics (speed, accuracy, disk usage), error analysis for archaic vocabulary, and practical recommendations for Arabic NLP projects.

## Features:

📊 Model Comparisons: Loading/transcription times, error rates, and resource usage.

🎯 Error Analysis: Common mistakes in diacritics (tashkeel) and classical Arabic terms.

📈 Visualizations: Speed-vs-accuracy trade-offs, disk footprint charts.

📜 Dataset: Audio samples from Mu'allaqat and benchmark results.

🛠️ Code: Python scripts for model loading, benchmarking, and visualization.

## Use Cases:

Academic research on classical Arabic ASR.

Optimizing Whisper models for Arabic poetry/dialects.

Resource-aware model selection for real-time transcription.

## Listen to Amr ibn Kulthum's Mu'allaqat  

Here’s an excerpt from the *Mu'allaqat*:  

<audio controls>
  <source src="01_AmroIbnKalthoum.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>


Here’s a YouTube video of Amr ibn Kulthum's *Mu'allaqat*:  
<video controls width="100%">
  <source src="[https://www.youtube.com/watch?v=QnEf85ksNlg](https://www.youtube.com/watch?v=QnEf85ksNlg)" type="video/mp4">
  Your browser does not support the video tag.
</video>

## *How to use*

```js
usage: transcribe.py [-h] --model {tiny,base,small,medium,large,turbo} --audio AUDIO [--language LANGUAGE]

Transcribe audio using OpenAI's Whisper model.

options:
  -h, --help            show this help message and exit
  --model {tiny,base,small,medium,large,turbo}
                        Model size to use for transcription (tiny, base, small, medium, large, turbo).
  --audio AUDIO         Path to the audio file to transcribe.
  --language LANGUAGE   Language code for transcription (e.g., 'ar' for Arabic).
```

```js
python transcribe.py --model turbo --audio 01_AmroIbnKalthoum.mp3 --language ar
```

```js
python whisper_benchmarks.py  
```

---

### **Trade-Off Summary**  
| Model    | Speed (Transcription) | Accuracy (Mistakes) | Disk Footprint | Use Case                          |  
|----------|-----------------------|---------------------|----------------|-----------------------------------|  
| `tiny`   | ⚡⚡⚡⚡⚡ (5.86s)       | ⚠️ 93 errors         | ⚡ 0.07 GB      | Real-time apps (speed > accuracy) |  
| `base`   | ⚡⚡⚡⚡ (14.37s)        | ⚠️ 41 errors         | ⚡ 0.14 GB      | Basic transcription               |  
| `small`  | ⚡⚡⚡ (30.28s)         | ⚠️ 28 errors         | ⚡ 0.46 GB      | Moderate accuracy needs           |  
| `medium` | ⚡⚡ (103.99s)          | ✅ 10 errors          | ⚡ 1.5 GB       | Balanced use cases                |  
| `large`  | ⚡ (115.54s)           | ✅ 7 errors           | ⚠️ 2.9 GB       | High accuracy (slow)              |  
| `turbo`  | ⚡⚡⚡ (64.29s)         | ✅✅ 6 errors          | ✅ 1.6 GB       | **Optimal choice**: Fast + accurate|  

---

### **Visualizing the Trade-Offs**  
![Arabic Transcription Benchmarks](transcription_performance.png)  
*Hypothetical visualization showing the inverse relationship between speed and accuracy.*

![Arabic Transcription Benchmarks](whisper_benchmarks_dark.png)  
 *Comparison of all metrics across models.*  

---

### **Analysis of Whisper Model Benchmarks for Arabic Transcription**  

### **1. Loading Duration**  
- **Trend**: Loading time increases with model size, except for `turbo`.  
- **Fastest**: `tiny` (0.66s)  
- **Slowest**: `large` (39.36s)  
- **Anomaly**: `turbo` loads **2.5x faster** than `large` (15.69s vs. 39.36s) despite similar accuracy.  

**Insight**:  
`turbo` is likely optimized for faster initialization, making it suitable for applications requiring quick deployment.

---

### **2. Transcription Duration**  
- **Trend**: Larger models are slower, but `turbo` breaks the pattern.  
- **Fastest**: `tiny` (5.86s)  
- **Slowest**: `large` (115.54s)  
- **Key Observation**: `turbo` transcribes **1.8x faster** than `large` (64.29s vs. 115.54s) with fewer errors.  

**Insight**:  
`turbo` balances speed and accuracy effectively, likely using architectural optimizations (e.g., pruning, quantization).

---

### **3. Disk Size**  
- **Trend**: Larger models require more storage.  
- **Smallest**: `tiny` (0.07 GB)  
- **Largest**: `large` (2.9 GB)  
- **Anomaly**: `turbo` is **45% smaller** than `large` (1.6 GB vs. 2.9 GB).  

**Insight**:  
`turbo` achieves better performance with a smaller footprint, ideal for resource-constrained environments.

---

### **4. Number of Mistakes**  
- **Trend**: Larger models make fewer errors.  
- **Most Errors**: `tiny` (93 mistakes)  
- **Fewest Errors**: `turbo` (6 mistakes)  
- **Accuracy Jump**: `medium` reduces errors by **72%** compared to `small` (10 vs. 28).  

**Insight**:  
For critical Arabic transcription tasks (e.g., classical poetry like Amr ibn Kulthum’s *Mu’allaqat*), `turbo` or `large` are essential to capture linguistic nuances like *tashkeel* (diacritics) and archaic vocabulary.

---

### **Key Takeaways for Arabic Transcription**  
1. **For Classical Poetry (e.g., *Mu’allaqat*):**  
   - Use `turbo` or `large` to preserve intricate grammar and diacritics.  

2. **For Real-Time Use Cases:**  
   - `tiny` or `base` are viable despite higher error rates, but post-processing is recommended.  

3. **Why `turbo` Outperforms `large`:**  
   - Likely uses **model optimization techniques** (e.g., distillation) to reduce size while retaining accuracy.  

4. **Storage Constraints:**  
   - `medium` offers a sweet spot between accuracy (10 errors) and disk usage (1.5 GB).  

---

### **Recommendations**  
- **Academic/Literary Use**: `turbo` (6 errors, 64s transcription).  
- **Real-Time Apps**: `tiny` + post-processing (e.g., rule-based error correction for Arabic diacritics).  
- **Balanced Workloads**: `medium` (10 errors, 104s).  

---

### **Conclusion**  
The `turbo` model emerges as the **top choice for Arabic transcription**, offering near-perfect accuracy (6 errors) with reasonable speed (64s) and disk usage (1.6 GB). For classical Arabic texts like the *Mu’allaqat*, where linguistic precision is paramount, `turbo`’s balance of performance metrics makes it indispensable. Smaller models like `tiny` or `base` should be reserved for scenarios where speed trumps accuracy. 
