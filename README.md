# AI Music Composer: End-to-End AI Application

## Overview
I developed **AI Music Composer**, a **production-ready AI application** that generates music with a specific style and mood using **LLM-driven prompts, music theory, and Python music libraries**.

This project demonstrates **full-stack AI engineering**, **cloud deployment**, **CI/CD pipelines**, and **interactive application development**, showcasing my ability to deliver **real-world, enterprise-grade AI solutions** — exactly what senior recruiters and technical leaders look for.

### Key Highlights
- Designed and implemented **prompt-driven music composition** for moods and styles (e.g., “sad beat with melody”).
- Generates **melodies, chord progressions, and rhythm durations** using Music21 and Synthesizer.
- **Fast setup** using **UV package manager** and `setup.sh` for deterministic dependency management.
- Built an **interactive UI** with Streamlit for instant user feedback.
- Fully **Dockerized** for reproducible environments.
- **Automated CI/CD pipeline** using GitLab, with cloud deployment on **GCP GAR + GKE (Free Tier)**.
- Integrated **NLP preprocessing** with SpaCy and NLTK to enhance prompt understanding.

---

## Tech Stack / Tools Used
| Layer | Tools / Libraries |
|-------|-----------------|
| Version Control & CI/CD | GitLab (Code versioning and automated pipelines) |
| Cloud Deployment | GCP – GAR (Artifact Registry), GKE (Kubernetes Free Tier) |
| AI / Music Libraries | Music21, Synthesizer, LangChain-Groq |
| NLP / ML | SpaCy, NLTK |
| UI / Frontend | Streamlit |
| Environment & Setup | UV + Docker |

---

## Quick Start

### 1. Clone the Repository
```bash
git clone https://gitlab.com/your-username/ai-music-composer.git
cd ai-music-composer
```

### 2. Run Setup
```bash
chmod +x setup.sh
./setup.sh
```
> This script installs all dependencies using **UV** for speed and reproducibility, builds the Docker container, and prepares the environment automatically.

### 3. Launch the Streamlit App
```bash
streamlit run main.py
```
- Enter a music prompt (e.g., “Compose a sad beat music with melody touch”).
- The AI generates **melody, chord progression, and rhythm patterns** in real time.

### Example Output
**Music Style:** Sad

**Generated Melody:**
```
C4 E4 G4 C4, E4 G4 A4 G4, G4 F#4 E4 D4, C4 E4 G4 C4
```
**Melody Description:**
- Descending arpeggio patterns convey sadness
- Minor thirds and major sevenths create a melancholic mood
- Variations and chromaticism add tension and release

**Chord Progression:**
```
Cm - G7 - Am - Em, Cm - G7 - F - G7, Am - Em - F - G7, Cm - G7 - Am - Em
```
**Rhythm Durations:**
```
C4: 1.0, E4: 0.5, G4: 0.5, C4: 1.0, ...
```
This demonstrates **AI-driven music composition** from textual prompts, suitable for interactive demos and production use.

---

## Deployment & CI/CD
I implemented a **fully automated deployment pipeline**:
- **GitLab CI/CD:** Builds, tests, and pushes Docker images.
- **GCP GAR + GKE:** Containerized app is deployed on a cloud-native Kubernetes cluster (Free Tier).
- **Dockerized Environment:** Ensures consistent behavior across local, CI/CD, and production.
- **UV + Docker:** Guarantees fast, deterministic setups.

---

## Future Enhancements
- Support for **multi-genre and multi-instrument compositions**.
- Enhanced **AI prompt understanding** with advanced NLP pipelines.
- Real-time collaborative music generation.
- Production-ready logging, monitoring, and analytics.
- Expanded **cloud deployment options** and horizontal scaling for enterprise use.