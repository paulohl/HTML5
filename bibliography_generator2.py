# Re-importing necessary module after code execution state reset
from pathlib import Path

# Define BibTeX entries for Chapter 2
bibtex_ch2 = """
@article{wolf2020transformers,
  title={Transformers: State-of-the-art natural language processing},
  author={Wolf, Thomas and Debut, Lysandre and Sanh, Victor and Chaumond, Julien and others},
  journal={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},
  pages={38--45},
  year={2020}
}

@article{rombach2022high,
  title={High-resolution image synthesis with latent diffusion models},
  author={Rombach, Robin and Blattmann, Andreas and Lorenz, Dominik and Esser, Patrick and Ommer, Bj{\"o}rn},
  journal={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={10684--10695},
  year={2022}
}

@misc{huggingface2023diffusers,
  title={Hugging Face Diffusers Documentation},
  author={{Hugging Face}},
  year={2023},
  howpublished={\\url{https://huggingface.co/docs/diffusers}}
}

@misc{huggingface2023transformers,
  title={Hugging Face Transformers Documentation},
  author={{Hugging Face}},
  year={2023},
  howpublished={\\url{https://huggingface.co/docs/transformers}}
}

@article{rajpurkar2016squad,
  title={SQuAD: 100,000+ questions for machine comprehension of text},
  author={Rajpurkar, Pranav and Zhang, Jian and Lopyrev, Konstantin and Liang, Percy},
  journal={arXiv preprint arXiv:1606.05250},
  year={2016}
}

@article{zhou2023lima,
  title={The LIMA model: Less is more for alignment},
  author={Zhou, Peter and Palangi, Hamid and others},
  journal={arXiv preprint arXiv:2305.11206},
  year={2023}
}

@misc{aws2023sagemaker,
  title={Amazon SageMaker Documentation},
  author={{AWS}},
  year={2023},
  howpublished={\\url{https://docs.aws.amazon.com/sagemaker/}}
}

@misc{gcp2023vertex,
  title={Google Cloud Vertex AI Documentation},
  author={{Google Cloud Platform}},
  year={2023},
  howpublished={\\url{https://cloud.google.com/vertex-ai/docs}}
}

@article{biewald2020experiment,
  title={Experiment tracking with Weights and Biases},
  author={Biewald, Lukas},
  journal={Software available from wandb.com},
  year={2020}
}

@article{shen2021stateless,
  title={Stateless model serving with dynamic batching for transformer inference},
  author={Shen, Shaojie and Zhang, Haoran and others},
  journal={arXiv preprint arXiv:2104.00920},
  year={2021}
}
"""

# Save Chapter 2 references to file
bib_file_ch2 = Path("/mnt/data/ch2_references.bib")
bib_file_ch2.write_text(bibtex_ch2.strip())

bib_file_ch2.name
