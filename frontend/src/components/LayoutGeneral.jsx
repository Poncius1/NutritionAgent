function LayoutGeneral({ children }) {
  return (
    <div className="min-h-screen bg-gradient-to-br from-nutrition-sky via-nutrition-teal to-white">
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-10 sm:py-12">
        {children}
      </div>
    </div>
  );
}

export default LayoutGeneral;