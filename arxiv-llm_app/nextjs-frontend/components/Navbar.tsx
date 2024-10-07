// components/Navbar.tsx

import Link from "next/link";

const Navbar: React.FC = () => {
  return (
    <nav>
      <div>
        <div className="p-4">
          <Link
            href="https://github.com/your-repo-url"
            className="text-black hover:underline p-4"
          >
            GitHub
          </Link>
          <Link href="/" className="text-black hover:underline p-4">
            Home
          </Link>
          <Link href="/ask" className="text-black hover:underline p-4">
            Ask a Question
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
