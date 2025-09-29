from pathlib import Path

# Define BibTeX entries for Chapter 1
bibtex_entries = """
@book{russell2021ai,
  title={Artificial Intelligence: A Modern Approach},
  author={Russell, Stuart and Norvig, Peter},
  year={2021},
  edition={4},
  publisher={Pearson}
}

@inproceedings{sommer2010outside,
  title={Outside the closed world: On using machine learning for network intrusion detection},
  author={Sommer, Robin and Paxson, Vern},
  booktitle={IEEE Symposium on Security and Privacy},
  pages={305--316},
  year={2010},
  organization={IEEE},
  doi={10.1109/SP.2010.25}
}

@article{vaswani2017attention,
  title={Attention is all you need},
  author={Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan N and Kaiser, Łukasz and Polosukhin, Illia},
  journal={Advances in neural information processing systems},
  volume={30},
  year={2017}
}

@article{brown2020language,
  title={Language models are few-shot learners},
  author={Brown, Tom B and Mann, Benjamin and Ryder, Nick and Subbiah, Melanie and others},
  journal={arXiv preprint arXiv:2005.14165},
  year={2020}
}

@article{ho2020ddpm,
  title={Denoising diffusion probabilistic models},
  author={Ho, Jonathan and Jain, Ajay and Abbeel, Pieter},
  journal={arXiv preprint arXiv:2006.11239},
  year={2020}
}

@article{brundage2020trustworthy,
  title={Toward trustworthy AI development: Mechanisms for supporting verifiable claims},
  author={Brundage, Miles and Avin, Shahar and Clark, Jack and others},
  journal={arXiv preprint arXiv:2004.07213},
  year={2020}
}

@book{leocadio2023diffusers,
  title={Hugging Face Diffusers: Architectures and Applications for AI and Reinforcement Learning},
  author={Leocadio, Paulo},
  year={2023}
}

@inproceedings{shokri2017membership,
  title={Membership inference attacks against machine learning models},
  author={Shokri, Reza and Stronati, Marco and Song, Congzheng and Shmatikov, Vitaly},
  booktitle={IEEE Symposium on Security and Privacy},
  pages={3--18},
  year={2017},
  organization={IEEE},
  doi={10.1109/SP.2017.41}
}

@misc{ibm2021databreach,
  title={The Cost of a Data Breach Report},
  author={{IBM Security}},
  year={2021},
  howpublished={\\url{https://www.ibm.com/reports/data-breach}}
}

@misc{mitre2022attack,
  title={ATT\&CK Framework Documentation},
  author={{MITRE}},
  year={2022},
  howpublished={\\url{https://attack.mitre.org/}}
}
"""

# Save to file
bib_file_path = Path("/mnt/data/ch1_references.bib")
bib_file_path.write_text(bibtex_entries.strip())

bib_file_path.name
