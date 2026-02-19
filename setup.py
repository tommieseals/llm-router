from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="llm-router",
    version="1.0.0",
    author="Tommie Seals",
    author_email="tommieseals@example.com",
    description="Intelligent LLM routing across multiple providers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tommieseals/llm-router",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.25.0",
        "python-dotenv>=0.19.0",
    ],
    extras_require={
        "dev": ["pytest", "pytest-cov", "black", "mypy"],
    },
    entry_points={
        "console_scripts": [
            "llm-router=llm_router.cli:main",
        ],
    },
)
