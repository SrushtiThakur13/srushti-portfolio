export default function Home() {
  return (
    <main className="px-8 py-12 max-w-6xl mx-auto">
      {/* Hero Section */}
      <section className="text-center py-16">
        <h1 className="text-5xl font-bold text-blue-600">
          Data Scientist & ML Engineer
        </h1>
        <p className="mt-4 text-lg text-gray-600">
          Transforming complex data into actionable insights with advanced machine learning, 
          improving model accuracy by 25% and reducing deployment latency by 40%.
        </p>
        <div className="mt-6 flex justify-center gap-4">
          <a
            href="mailto:srushtithakur.ds@gmail.com"
            className="bg-blue-600 text-white px-4 py-2 rounded"
          >
            Get In Touch
          </a>
          <a
            href="https://github.com/SrushtiThakur13"
            target="_blank"
            className="border px-4 py-2 rounded"
          >
            View GitHub
          </a>
        </div>
      </section>

      {/* About Section */}
      <section className="py-12">
        <h2 className="text-3xl font-semibold mb-4">About Me</h2>
        <p className="text-gray-700 leading-relaxed">
          I&apos;m a passionate Data Scientist at Morgan Stanley with expertise in machine
          learning, forecasting, and anomaly detection. With a Master&apos;s in Electrical
          Engineering (ML) from San Jose State University, I specialize in building scalable
          ML solutions that drive business impact.
        </p>
      </section>

      {/* Projects Section */}
      <section className="py-12">
        <h2 className="text-3xl font-semibold mb-8">Featured Projects</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {/* Project 1 */}
          <div className="p-6 border rounded-lg shadow">
            <h3 className="text-xl font-bold mb-2">Cancer Detection CNN</h3>
            <p className="text-gray-600 mb-2">
              Deep learning model for automated cancer detection with strong performance.
            </p>
            <a
              href="https://github.com/SrushtiThakur13/srushti-portfolio/tree/main/cancer-detection-cnn"
              target="_blank"
              className="text-blue-600 underline"
            >
              View Code
            </a>
          </div>

          {/* Project 2 */}
          <div className="p-6 border rounded-lg shadow">
            <h3 className="text-xl font-bold mb-2">E-Commerce Generative AI</h3>
            <p className="text-gray-600 mb-2">
              Fine-tuned Falcon LLM for scalable product recommendations.
            </p>
            <a
              href="https://github.com/SrushtiThakur13/srushti-portfolio/tree/main/ecommerce-generative-ai"
              target="_blank"
              className="text-blue-600 underline"
            >
              View Code
            </a>
          </div>

          {/* Project 3 */}
          <div className="p-6 border rounded-lg shadow">
            <h3 className="text-xl font-bold mb-2">Fraud Detection</h3>
            <p className="text-gray-600 mb-2">
              Real-time anomaly detection for financial fraud prevention.
            </p>
            <a
              href="https://github.com/SrushtiThakur13/srushti-portfolio/tree/main/fraud-detection"
              target="_blank"
              className="text-blue-600 underline"
            >
              View Code
            </a>
          </div>

          {/* Project 4 */}
          <div className="p-6 border rounded-lg shadow">
            <h3 className="text-xl font-bold mb-2">Sentiment Analysis</h3>
            <p className="text-gray-600 mb-2">
              NLP pipeline for classifying positive/negative reviews with wordcloud visuals.
            </p>
            <a
              href="https://github.com/SrushtiThakur13/srushti-portfolio/tree/main/sentiment-analysis"
              target="_blank"
              className="text-blue-600 underline"
            >
              View Code
            </a>
          </div>

          {/* Project 5 */}
          <div className="p-6 border rounded-lg shadow">
            <h3 className="text-xl font-bold mb-2">Time Series Forecasting</h3>
            <p className="text-gray-600 mb-2">
              LSTM-based forecasting with fine-tuning for business metrics.
            </p>
            <a
              href="https://github.com/SrushtiThakur13/srushti-portfolio/tree/main/time-series-forecasting"
              target="_blank"
              className="text-blue-600 underline"
            >
              View Code
            </a>
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section className="py-12 text-center">
        <h2 className="text-3xl font-semibold mb-4">Let&apos;s Connect</h2>
        <p className="mb-4">
          Ready to discuss data science opportunities or collaborate on ML projects?
        </p>
        <div className="flex justify-center gap-8">
          <a href="mailto:srushtithakur.ds@gmail.com" className="underline">
            📧 Email
          </a>
          <a href="tel:+16692231386" className="underline">
            📞 Phone
          </a>
          <a href="https://github.com/SrushtiThakur13" target="_blank" className="underline">
            🖥 GitHub
          </a>
        </div>
      </section>
    </main>
  );
}
