[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

# Talking-Face Research Papers (With GPT Analysis)
> Updated on 2024.01.27
Current Search Keywords: `Talking Face`, `Talking Head`, `Visual Dubbing`, `Face Genertation`, `Lip Sync`, `Talker`, `Portrait`, `Talking Video`, `Head Synthesis`, `Face Reenactment`, `Wav2Lip`, `Talking Avatar`, `Lip Generation`, `Lip-Synchronization`, `Portrait Animation`, `Facial Animation`, `Lip Expert`

> If you have any other keywords, please feel free to let us know :) 

> We now offer support for article analysis through large language models. You can view this feature by clicking the `Paper Analysis` link below. Currently, we are experimenting with `Claude.ai` and plan to also integrate `GPT-4-turbo` for a comparative analysis of articles. This is to help everyone **quickly skim** through the latest research papers. 

 

<details>
  <summary>Recent Trends (by Claude.ai)</summary>
  <ol>
    <li> Based on analyzing the collection of academic papers on talking face generation, here is a summary of five prominent recent trends and developments:

<b>Neural radiance fields (NeRFs)</b>: Many recent papers explore using neural radiance fields to represent talking faces in 3D. NeRFs can model view-dependent effects and complex geometry. Papers show NeRFs can achieve photo-realistic reconstruction and animation of talking heads from images or video. However, most methods require expensive per-person training. Recent trends look to make NeRF talking faces generalizable in a one-shot setting.

<b>Generative models</b>: Generative adversarial networks (GANs) and variational autoencoders (VAEs) are popular for modeling talking faces. They can synthesize video frames conditioned on audio or motion. Diffusion models are an emerging trend, as they can generate sharper results and enable new applications like face editing. Recent papers also explore ways to control emotion, pose, expression, and other attributes of generated talking faces.

<b>Controllable generation</b>: Many papers focus on controlling aspects of talking face generation like speech, expression, gaze, and head pose. This includes disentangling factors of variation and learning interpretable controls. Recent trends use conditioned models like NeRFs to enable control over viewpoints. There is also interest in controlling generation using natural language prompts.

<b>Limited data</b>: A prevalent trend is reducing data requirements for talking face models through transfer learning, few-shot adaptation, and pretraining. This allows high-quality controllable talking faces to be synthesized for new people with less data. Approaches leverage 3D priors, perceptual losses, and modularity to improve data efficiency.

<b>Full avatar generation</b>: Recent papers are beginning to address generating full avatars rather than just the face region. This includes modeling the torso, shoulders, background, and body gestures to accompany speech. The focus is on natural motion and seamless transitions between spontaneous and non-spontaneous movements to improve realism.</li>
  </ol>
</details>

[>>>> Each Paper Analysis (by Claude.ai) <<<<](https://github.com/liutaocode/talking-face-arxiv-daily/blob/main/analysis_by_claude_ai.md) 

[Web Page](https://liutaocode.github.io/talking-face-arxiv-daily/) ([Scrape Code](https://github.com/liutaocode/talking-face-arxiv-daily)) 

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href=#talking-face>Talking Face</a></li>
    <li><a href=#image-animation>Image Animation</a></li>
  </ol>
</details>

## Talking Face

- 2023-12-23, **TransFace: Unit-Based Audio-Visual Speech Synthesizer for Talking Head Translation**, Xize Cheng et.al., Paper: [http://arxiv.org/abs/2312.15197](http://arxiv.org/abs/2312.15197)
- 2024-01-02, **Towards a Simultaneous and Granular Identity-Expression Control in Personalized Face Generation**, Renshuai Liu et.al., Paper: [http://arxiv.org/abs/2401.01207](http://arxiv.org/abs/2401.01207)
- 2023-12-25, **SAiD: Speech-driven Blendshape Facial Animation with Diffusion**, Inkyu Park et.al., Paper: [http://arxiv.org/abs/2401.08655](http://arxiv.org/abs/2401.08655), Code: **[https://github.com/yunik1004/said](https://github.com/yunik1004/said)**
- 2024-01-20, **Real3D-Portrait: One-shot Realistic 3D Talking Portrait Synthesis**, Zhenhui Ye et.al., Paper: [http://arxiv.org/abs/2401.08503](http://arxiv.org/abs/2401.08503)
- 2024-01-23, **NeRF-AD: Neural Radiance Field with Attention-based Disentanglement for Talking Face Synthesis**, Chongke Bi et.al., Paper: [http://arxiv.org/abs/2401.12568](http://arxiv.org/abs/2401.12568)
- 2024-01-11, **Jump Cut Smoothing for Talking Heads**, Xiaojuan Wang et.al., Paper: [http://arxiv.org/abs/2401.04718](http://arxiv.org/abs/2401.04718)
- 2024-01-07, **Freetalker: Controllable Speech and Text-Driven Gesture Generation Based on Diffusion Models for Enhanced Speaker Naturalness**, Sicheng Yang et.al., Paper: [http://arxiv.org/abs/2401.03476](http://arxiv.org/abs/2401.03476)
- 2024-01-19, **Fast Registration of Photorealistic Avatars for VR Facial Animation**, Chaitanya Patel et.al., Paper: [http://arxiv.org/abs/2401.11002](http://arxiv.org/abs/2401.11002)
- 2024-01-18, **Exposing Lip-syncing Deepfakes from Mouth Inconsistencies**, Soumyya Kanti Datta et.al., Paper: [http://arxiv.org/abs/2401.10113](http://arxiv.org/abs/2401.10113)
- 2024-01-16, **EmoTalker: Emotionally Editable Talking Face Generation via Diffusion Model**, Bingyuan Zhang et.al., Paper: [http://arxiv.org/abs/2401.08049](http://arxiv.org/abs/2401.08049)
- 2024-01-08, **EFHQ: Multi-purpose ExtremePose-Face-HQ dataset**, Trung Tuan Dao et.al., Paper: [http://arxiv.org/abs/2312.17205](http://arxiv.org/abs/2312.17205)
- 2024-01-11, **Dubbing for Everyone: Data-Efficient Visual Dubbing using Neural Rendering Priors**, Jack Saunders et.al., Paper: [http://arxiv.org/abs/2401.06126](http://arxiv.org/abs/2401.06126)
- 2023-12-21, **DREAM-Talk: Diffusion-based Realistic Emotional Audio-driven Method for Single Image Talking Face Generation**, Chenxu Zhang et.al., Paper: [http://arxiv.org/abs/2312.13578](http://arxiv.org/abs/2312.13578)

<p align=right>(<a href=#updated-on-20240127>back to top</a>)</p>

## Image Animation

- 2023-12-21, **PIA: Your Personalized Image Animator via Plug-and-Play Modules in Text-to-Image Models**, Yiming Zhang et.al., Paper: [http://arxiv.org/abs/2312.13964](http://arxiv.org/abs/2312.13964), Code: **[https://github.com/open-mmlab/PIA](https://github.com/open-mmlab/PIA)**
- 2023-11-30, **Motion-Conditioned Image Animation for Video Editing**, Wilson Yan et.al., Paper: [http://arxiv.org/abs/2311.18827](http://arxiv.org/abs/2311.18827)
- 2024-01-03, **Moonshot: Towards Controllable Video Generation and Editing with Multimodal Conditions**, David Junhao Zhang et.al., Paper: [http://arxiv.org/abs/2401.01827](http://arxiv.org/abs/2401.01827), Code: **[https://github.com/salesforce/lavis](https://github.com/salesforce/lavis)**
- 2023-11-27, **MagicAnimate: Temporally Consistent Human Image Animation using Diffusion Model**, Zhongcong Xu et.al., Paper: [http://arxiv.org/abs/2311.16498](http://arxiv.org/abs/2311.16498)
- 2023-12-05, **LivePhoto: Real Image Animation with Text-guided Motion Control**, Xi Chen et.al., Paper: [http://arxiv.org/abs/2312.02928](http://arxiv.org/abs/2312.02928)
- 2023-10-16, **LAMP: Learn A Motion Pattern for Few-Shot-Based Video Generation**, Ruiqi Wu et.al., Paper: [http://arxiv.org/abs/2310.10769](http://arxiv.org/abs/2310.10769), Code: **[https://github.com/RQ-Wu/LAMP](https://github.com/RQ-Wu/LAMP)**
- 2023-11-27, **DynamiCrafter: Animating Open-domain Images with Video Diffusion Priors**, Jinbo Xing et.al., Paper: [http://arxiv.org/abs/2310.12190](http://arxiv.org/abs/2310.12190), Code: **[https://github.com/Doubiiu/DynamiCrafter](https://github.com/Doubiiu/DynamiCrafter)**
- 2024-01-17, **Continuous Piecewise-Affine Based Motion Model for Image Animation**, Hexiang Wang et.al., Paper: [http://arxiv.org/abs/2401.09146](http://arxiv.org/abs/2401.09146), Code: **[https://github.com/devilpg/aaai2024-cpabmm](https://github.com/devilpg/aaai2024-cpabmm)**
- 2023-12-06, **AnimateZero: Video Diffusion Models are Zero-Shot Image Animators**, Jiwen Yu et.al., Paper: [http://arxiv.org/abs/2312.03793](http://arxiv.org/abs/2312.03793), Code: **[https://github.com/vvictoryuki/animatezero](https://github.com/vvictoryuki/animatezero)**
- 2023-12-04, **AnimateAnything: Fine-Grained Open Domain Image Animation with Motion Guidance**, Zuozhuo Dai et.al., Paper: [http://arxiv.org/abs/2311.12886](http://arxiv.org/abs/2311.12886), Code: **[https://github.com/alibaba/animate-anything](https://github.com/alibaba/animate-anything)**

<p align=right>(<a href=#updated-on-20240127>back to top</a>)</p>

Notes: 

* We have modified the `sorting rule` of the above table to prioritize papers based on the time of their latest update rather than their initial publication date. If an article has been recently modified, it will appear earlier in the list. 

* However, recent trends are still based on `ten` papers sorted by the initial publication date. 

Function added: 

* Support more reliable text parser. [Link](https://github.com/pdfminer/pdfminer.six) 

* Support rich markdown format (better at parsing experimental tables). [Link](https://github.com/davendw49/sciparser) 

* Supports the analysis of more than 10 papers in a single conversation, which exceeds the attachment size limit. 

[contributors-shield]: https://img.shields.io/github/contributors/liutaocode/talking-face-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/liutaocode/talking-face-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/liutaocode/talking-face-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/liutaocode/talking-face-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/liutaocode/talking-face-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/liutaocode/talking-face-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/liutaocode/talking-face-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/liutaocode/talking-face-arxiv-daily/issues

